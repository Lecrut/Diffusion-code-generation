import sys
if __name__ == '__main__':
    length_data = [10, 20, 30, 40, 50]
    results = []
    for i in range(len(length_data) - 1):
        ratio = length_data[i+1] / length_data[i]
        results.append((length_data[i], length_data[i+1], ratio))
    print("Length A, Length B, Ratio")
    print("------------------------")
    for a, b, r in results:
        print(f"{a}, {b}, {r:.4f}")