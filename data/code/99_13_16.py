class FlagProcessor:
    AND = 'and'
    OR = 'or'

    @staticmethod
    def process_flags(flag_a, flag_b, operator):
        if operator == FlagProcessor.AND:
            return flag_a and flag_b
        elif operator == FlagProcessor.OR:
            return flag_a or flag_b
        else:
            raise ValueError('Unsupported operator')

if __name__ == '__main__':
    processor = FlagProcessor()
    print(processor.process_flags(True, False, FlagProcessor.AND))
    print(processor.process_flags(True, True, FlagProcessor.OR))