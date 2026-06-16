import itertools
def alternate_streams(numbers, strings):
    output = []
    for num, s in zip(numbers, strings):
        output.append(str(num))
        output.append(s)
    return "".join(output)
if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5]
    strings = ["A", "B", "C", "D", "E"]
    result = alternate_streams(numbers, strings)
    print(result)