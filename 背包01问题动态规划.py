good = ["1", "2", "3", "4", "5"]
good_weight = [15, 5, 68, 31, 20]
good_profit = [20, 6, 4, 8, 75]
box_space = 100

# 初始化dp数组,dp[i][j] 表示前 i 个物品在背包容量为 j 时的最大总价值
dp = [[0 for _ in range(box_space + 1)] for _ in range(len(good) + 1)]


for i in range(1,len(good)+1):
    for j in range(1,box_space+1):
        if good_weight[i-1] > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j],good_profit[i-1]+dp[i-1][j-good_weight[i-1]])

selected_goods = []
i = len(good)
j = box_space

while i > 0 and j > 0:
    # 如果dp[i][j]不等于dp[i-1][j]，则说明第i个物品被选择
    if dp[i][j] != dp[i-1][j]:
        selected_goods.append(good[i-1])
        j -= good_weight[i-1]
    i -= 1

selected_goods.reverse()  # 反转列表以获得正确的顺序
print("选择的货物名单:", selected_goods)


# 最大价值
max_profit = dp[len(good)][box_space]
print("最大价值为:", max_profit)

