def generate_nine_times_table():
    results = []
    for i in range(1, 13):
        result = f"{i} x 9 = {i * 9}"
        results.append(result)
    return results

if __name__ == '__main__':
    table = generate_nine_times_table()
    for line in table:
        print(line)