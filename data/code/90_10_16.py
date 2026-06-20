class DecisionMaker:
    MIN_AGE = 18
    REQUIRED_IDENTITY_VERIFIED = True

    @staticmethod
    def evaluate(age, identity_verified):
        return age >= DecisionMaker.MIN_AGE or identity_verified == DecisionMaker.REQUIRED_IDENTITY_VERIFIED

if __name__ == '__main__':
    decision_maker = DecisionMaker()
    result1 = decision_maker.evaluate(20, False)
    print(f"Result for age=20, identity verified=False: {result1}")

    result2 = decision_maker.evaluate(15, True)
    print(f"Result for age=15, identity verified=True: {result2}")