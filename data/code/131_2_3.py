class DecisionMaker:
    def evaluate(self, data, rules):
        decision = "No decision found"
        for rule in rules:
            if rule['condition'] == data:
                decision = rule['outcome']
                break
        return decision
if __name__ == '__main__':
    decision_maker = DecisionMaker()
    sample_data = "High"
    sample_rules = [
        {'condition': "Low", 'outcome': "Low Priority"},
        {'condition': "Medium", 'outcome': "Medium Priority"},
        {'condition': "High", 'outcome': "High Priority"}
    ]
    result = decision_maker.evaluate(sample_data, sample_rules)
    print(result)