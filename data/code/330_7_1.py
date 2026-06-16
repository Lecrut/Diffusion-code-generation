import string
def repeatedly_uppercase(s, n):
    result = s
    for _ in range(n):
        result = result.upper()
    return result
if __name__ == '__main__':
    sample_string = "hello"
    num_applications = 3
    final_result = repeatedly_uppercase(sample_string, num_applications)
    print(final_result)