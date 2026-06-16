def apply_uppercase_repeatedly(s, n):
    result = s
    for _ in range(n):
        result = result.upper()
    return result
if __name__ == '__main__':
    sample_string = "hello"
    num_repetitions = 3
    final_result = apply_uppercase_repeatedly(sample_string, num_repetitions)
    print(final_result)