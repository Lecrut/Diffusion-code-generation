def find_largest_number(input_string):
    numbers = []
    for item in input_string.split(','):
        try:
            number = float(item.strip())
            numbers.append(number)
        except ValueError:
            continue
    if not numbers:
        return None
    return max(numbers)
if __name__ == '__main__':
    sample1 = "10,5,22,8"
    print(f"Input: '{sample1}', Largest: {find_largest_number(sample1)}")
    sample2 = "3.14,1.618,2.718"
    print(f"Input: '{sample2}', Largest: {find_largest_number(sample2)}")
    sample3 = "a,b,100,c"
    print(f"Input: '{sample3}', Largest: {find_largest_number(sample3)}")
    sample4 = "50"
    print(f"Input: '{sample4}', Largest: {find_largest_number(sample4)}")
    sample5 = ""
    print(f"Input: '{sample5}', Largest: {find_largest_number(sample5)}")