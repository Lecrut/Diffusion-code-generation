class DeMorganVerifier:
    BOOL_VALUES = [False, True]

    @staticmethod
    def verify_de_morgan_laws():
        results = []
        for A in DeMorganVerifier.BOOL_VALUES:
            for B in DeMorganVerifier.BOOL_VALUES:
                left_side = (A and B)
                right_side = not (not A or not B)
                results.append((A, B, left_side == right_side))
        return results

if __name__ == '__main__':
    print(DeMorganVerifier.verify_de_morgan_laws())