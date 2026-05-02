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
    print("Length Ratio Table")
    print("--------------------")
    print(f"{'Length 1':<10}{'Length 2':<10}{'Ratio':<10}")
    for num1, num2, ratio in results:
        print(f"{num1:<10}{num2:<10}{ratio:<10.4f}")