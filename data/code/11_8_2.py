import sys
if __name__ == '__main__':
    data = [10, 20, 30, 40, 50]
    results = []
    for i in range(len(data) - 1):
        numerator = data[i]
        denominator = data[i+1]
        if denominator != 0:
            ratio = numerator / denominator
            results.append((numerator, denominator, ratio))
        else:
            results.append((numerator, denominator, float('inf')))
    print("Numerator | Denominator | Ratio")
    print("----------|-------------|------")
    for num, den, ratio in results:
        print(f"{num:9} | {den:11} | {ratio:.4f}")