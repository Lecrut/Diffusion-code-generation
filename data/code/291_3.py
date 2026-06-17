def compare_strings(str1, str2):
    if len(str1) > len(str2):
        print(f"{str1} is longer than {str2}")
    elif len(str2) > len(str1):
        print(f"{str2} is longer than {str1}")
    else:
        print(f"{str1} and {str2} are the same length")
if __name__ == '__main__':
    string_a = "hello"
    string_b = "world"
    compare_strings(string_a, string_b)
    string_c = "programming"
    string_d = "python"
    compare_strings(string_c, string_d)
    string_e = "test"
    string_f = "testing"
    compare_strings(string_e, string_f)