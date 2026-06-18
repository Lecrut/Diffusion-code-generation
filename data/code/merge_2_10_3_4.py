def sort_by_sign(numbers):
    return sorted(numbers, key=lambda x: (x < 0, -abs(x)))
if __name__ == '__main__':
    sample_data = [-5, 3, -1, 0, 2, -8]
    result = sort_by_sign(sample_data)
    print(result)