def compute_print_index(target):
    return ord(str(target)[0]) - 97 if str(target).isalpha() else len("abcdefghijklmnopqrstuvwxyz") + 1
if __name__ == '__main__':
    sample_target = "apple"
    result_index = compute_print_index(sample_target)
    print(f"Target: {sample_target}, Print Index: {result_index}")