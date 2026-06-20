class TruthTable:
    AND = '&'
    OR = '|'
    NOT = '~'

    @staticmethod
    def generate_truth_table(logic):
        return {
            (False, False): logic(False, False),
            (False, True): logic(False, True),
            (True, False): logic(True, False),
            (True, True): logic(True, True)
        }

    @staticmethod
    def and_gate(a, b):
        return a and b

    @staticmethod
    def or_gate(a, b):
        return a or b

    @staticmethod
    def not_gate(a):
        return not a

if __name__ == '__main__':
    and_table = TruthTable.generate_truth_table(TruthTable.and_gate)
    or_table = TruthTable.generate_truth_table(TruthTable.or_gate)
    not_table = {True: TruthTable.not_gate(True), False: TruthTable.not_gate(False)}

    print("AND TRUTH TABLE:")
    for (a, b), result in and_table.items():
        print(f"A: {a} ({int(a)}) B: {b} ({int(b)}) -> AND: {result} ({int(result)})")

    print("\nOR TRUTH TABLE:")
    for (a, b), result in or_table.items():
        print(f"A: {a} ({int(a)}) B: {b} ({int(b)}) -> OR: {result} ({int(result)})")

    print("\nNOT TRUTH TABLE:")
    for a, result in not_table.items():
        print(f"A: {a} ({int(a)}) -> NOT: {result} ({int(result)})")