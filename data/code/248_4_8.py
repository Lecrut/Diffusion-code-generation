class AdditionRoutine:
    def add(self, a: int, b: int) -> int:
        return a + b

if __name__ == '__main__':
    routine = AdditionRoutine()
    result = routine.add(3, 5)
    print(result)