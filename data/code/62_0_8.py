def compute_divisors(number):
    limit = int(number**0.5)
    small_divs = []
    large_divs = []
    index = 1
    while index <= limit:
        if number % index == 0:
            small_divs.append(index)
            if index != number // index:
                large_divs.append(number // index)
        index += 1
    large_divs.reverse()
    return small_divs + large_divs

if __name__ == '__main__':
    sample_value = 36
    output = compute_divisors(sample_value)
    print(output)