def reverse_list(lst):
    return lst[::-1]

if __name__ == '__main__':
    sample = [7, 8, 9, 10]
    reversed_sample = reverse_list(sample)
    print(f"Original: {sample}")
    print(f"Reversed: {reversed_sample}")