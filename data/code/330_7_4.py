def repeatedly_uppercase(s, n):
    result = s
    for _ in range(n):
        result = result.upper()
    return result
if __name__ == '__main__':
    string_to_transform = "hello"
    number_of_applications = 3
    final_result = repeatedly_uppercase(string_to_transform, number_of_applications)
    print(final_result)