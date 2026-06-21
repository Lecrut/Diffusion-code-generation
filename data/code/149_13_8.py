class Reverser:
    def reverse(self, iterable):
        return list(iterable[::-1])

if __name__ == '__main__':
    reverser = Reverser()
    print(reverser.reverse([1, 2, 3, 4, 5]))
    print(reverser.reverse((6, 7, 8, 9)))
    print(reverser.reverse("ABCDE"))