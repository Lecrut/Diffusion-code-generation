def generate_nine_multiplication_table():
    results = []
    for i in range(1, 11):
        results.append(f"{i} x 9 = {i * 9}")
    return results

if __name__ == '__main__':
    for line in generate_nine_multiplication_table():
        print(line)