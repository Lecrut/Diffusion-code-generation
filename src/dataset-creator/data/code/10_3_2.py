def sort_by_sign(numbers):
    return sorted(numbers, key=lambda x: (x < 0, -abs(x)))
if __name__ == '__main__':
    sample_data = [-5, 3, -12, 7, -89, 0, 4]
    result = sort_by_sign(sample_data)
    print(result)