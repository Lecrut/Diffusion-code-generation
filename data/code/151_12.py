import time
list1 = [1, 2, 3]
list2 = [4, 5, 6]
def combine_with_plus():
    result = list1 + list2
    print("Result using + operator:", result)
def combine_with_extend():
    result = list1[:]
    result.extend(list2)
    print("Result using extend():", result)
def combine_with_comprehension():
    result = [x for x in list1] + [x for x in list2]
    print("Result using list comprehension:", result)
if __name__ == '__main__':
    start_time = time.time()
    combine_with_plus()
    combine_with_extend()
    combine_with_comprehension()
    end_time = time.time()
    print(f"\nTotal execution time: {end_time - start_time} seconds")