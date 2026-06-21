def extract_odds(numbers):
    odd_list = []
    for number in numbers:
        if number & 1:
            odd_list.append(number)
    return odd_list

if __name__ == '__main__':
    sample_values = [24, 35, 46, 57, 68, 69, 70]
    print(extract_odds(sample_values))