lst = [-12, 25, -36, 23, -1]
result = 0


for i in range(4):
    if i % 2 == 0:
        result += lst[i]
    else:
        result = lst[i] - result

print(result * lst[4])