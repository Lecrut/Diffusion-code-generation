class FlagProcessor:
    def __init__(self, flag1, flag2):
        self.flag1 = flag1
        self.flag2 = flag2

    def process_flags(self):
        return self.flag1 and self.flag2

if __name__ == '__main__':
    processor = FlagProcessor(True, False)
    result = processor.process_flags()
    print(result)