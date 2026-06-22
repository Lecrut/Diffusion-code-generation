def check_number(n):
    results = []
    if n > 0:
        results.append("positive")
    else:
        results.append("not positive")
    if n % 2 == 0:
        results.append("even")
    else:
        results.append("odd")
    if n < 100:
        results.append("less than 100")
    else:
        results.append("not less than 100")
    return ", ".join(results)

if __name__ == '__main__':
    sample_values = [50, -10, 105, 99]
    for val in sample_values:
        print(check_number(val))