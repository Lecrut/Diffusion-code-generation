def find_opposite_truth(truth):
    return not truth

if __name__ == '__main__':
    sample3 = True
    opposite_sample3 = find_opposite_truth(sample3)
    print(f"Opposite of {sample3} is {opposite_sample3}")
    
    sample4 = False
    opposite_sample4 = find_opposite_truth(sample4)
    print(f"Opposite of {sample4} is {opposite_sample4}")