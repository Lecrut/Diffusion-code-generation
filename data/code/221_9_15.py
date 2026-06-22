class Sorter:

    def sort(self, a, b, c):
        if a > b:
            temp = a
            a = b
            b = temp
        if a > c:
            temp = a
            a = c
            c = temp
        if b > c:
            temp = b
            b = c
            c = temp
        return (a, b, c)
if __name__ == '__main__':
    sorter = Sorter()
    result = sorter.sort(3, 1, 2)
    print(result)