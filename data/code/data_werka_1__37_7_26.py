def concatenate_with_space(s1, s2):
    return f"{s1} {s2}"

if __name__ == '__main__':
    first_string = "Alibaba"
    second_string = "Cloud"
    combined_result = concatenate_with_space(first_string, second_string)
    print(combined_result)