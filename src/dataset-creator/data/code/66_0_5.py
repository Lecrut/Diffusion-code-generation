import sys
def calculate_weight_differences(items):
    if len(items) < 2:
        return []
    diffs = []
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            diff = abs(items[i] - items[j])
            diffs.append(round(diff, 6))
    return sorted(diffs)
def main():
    sample_items = [10.5, 20.7, 30.9, 40.8]
    differences = calculate_weight_differences(sample_items)
    print(f"Sample items: {sample_items}")
    print("Weight differences (sorted):")
    for idx, diff in enumerate(differences, start=1):
        print(f"{idx}. {diff:.6f}")
if __name__ == '__main__':
    main()