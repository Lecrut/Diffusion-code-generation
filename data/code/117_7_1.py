def compute_differences(numbers, reference):
    return [n - reference for n in numbers]
if __name__ == '__main__':
    data = [10, 25, 5, 40, 15]
    ref = 20
    result = compute_differences(data, ref)
    print(result)