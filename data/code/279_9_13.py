class DivisibleByThreeAndFive:
    def print_divisibles(self):
        for i in range(1, 101):
            if i % 3 == 0 and i % 5 == 0:
                print(i)

if __name__ == '__main__':
    instance = DivisibleByThreeAndFive()
    instance.print_divisibles()