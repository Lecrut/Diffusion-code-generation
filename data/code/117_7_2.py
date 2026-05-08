def compute_differences(numbers, reference):
    return [n - reference for n in numbers]
if __name__ == '__main__':
    data = [10, 25, 32, 48, 55]
    ref = 30
    result = compute_differences(data, ref)
    print(result)