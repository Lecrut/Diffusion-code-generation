class NumberChecker:

    def __init__(self, value):
        self.value = value

    def compare_to(self, other):
        return self.value > other.value
if __name__ == '__main__':
    instance1 = NumberChecker(20)
    instance2 = NumberChecker(15)
    instance3 = NumberChecker(5)
    result1 = instance1.compare_to(instance2)
    print(f'Is {instance1.value} greater than {instance2.value}? {result1}')
    result2 = instance2.compare_to(instance3)
    print(f'Is {instance2.value} greater than {instance3.value}? {result2}')
    result3 = instance3.compare_to(instance1)
    print(f'Is {instance3.value} greater than {instance1.value}? {result3}')