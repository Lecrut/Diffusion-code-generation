import string
def apply_uppercase_repeatedly(s, n):
    result = s
    for _ in range(n):
        result = result.upper()
    return result
if __name__ == '__main__':
    sample_string = "hello"
    num_applications = 3
    final_result = apply_uppercase_repeatedly(sample_string, num_applications)
    print(final_result)