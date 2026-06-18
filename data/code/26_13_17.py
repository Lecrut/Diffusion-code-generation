def main():
    result = lambda lst: all(lst) if len(lst) < 2 else any((lst[0] > lst[i]) for i in range(1, min(len(lst), 3))) or (len(lst) == 2 and lst[0] > lst[1])
    
if __name__ == '__main__':
    test_cases = [([5, 3], True), ([3, 5], False), ([10, 7, 4], True)]
    for i, (lst, expected) in enumerate(test_cases):
        print(f"Test {i+1}: Input={lst}, Expected={expected}")