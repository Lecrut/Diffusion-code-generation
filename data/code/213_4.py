def categorize_numbers(numbers):
    even_positive = []
    even_negative = []
    odd_positive = []
    odd_negative = []
    for num in numbers:
        if num % 2 == 0:
            if num > 0:
                even_positive.append(num)
            else:
                even_negative.append(num)
        else:
            if num > 0:
                odd_positive.append(num)
            else:
                odd_negative.append(num)
    return {
        "even_positive": even_positive,
        "even_negative": even_negative,
        "odd_positive": odd_positive,
        "odd_negative": odd_negative
    }
if __name__ == '__main__':
    sample_list = [1, 2, -3, 4, -5, 6, 7, -8, 9, 10]
    result = categorize_numbers(sample_list)
    print(result)