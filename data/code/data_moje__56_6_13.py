def generate_nine_multiplication_rows(count):
    for i in range(1, count + 1):
        yield 9 * i

if __name__ == '__main__':
    sample_count = 10
    results = list(generate_nine_multiplication_rows(sample_count))
    print(results)