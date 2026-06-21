def find_max_of_three(first, second, third):
    larger = first if first > second else second
    return third if third > larger else larger

if __name__ == '__main__':
    a = 7
    b = 23
    c = 11
    peak = find_max_of_three(a, b, c)
    print(peak)