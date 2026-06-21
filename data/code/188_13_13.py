def reverse_list(lst):
    return lst[::-1]

if __name__ == '__main__':
    sample = [7, 8, 9, 10]
    print(f"Original: {sample}")
    reversed_sample = reverse_list(sample)
    print(f"Reversed: {reversed_sample}")