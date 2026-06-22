def greatest_of_three(first, second, third):
    leader = first
    if second > leader:
        leader = second
    if third > leader:
        leader = third
    return leader

if __name__ == '__main__':
    sample_a = 5
    sample_b = 12
    sample_c = 8
    output = greatest_of_three(sample_a, sample_b, sample_c)
    print(output)