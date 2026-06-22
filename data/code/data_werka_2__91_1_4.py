class BooleanProcessor:
    @classmethod
    def invert(cls, flag: bool) -> bool:
        return not flag

if __name__ == '__main__':
    processor = BooleanProcessor()
    true_result = processor.invert(True)
    false_result = processor.invert(False)
    print(true_result)
    print(false_result)