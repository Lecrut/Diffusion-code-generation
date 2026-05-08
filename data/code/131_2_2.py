class DecisionMaker:
    def evaluate(self, data, rules):
        decision = "No decision found"
        for rule in rules:
            if rule['condition'] == data:
                decision = rule['outcome']
                break
        return decision
if __name__ == '__main__':
    dm = DecisionMaker()
    sample_data = "High"
    sample_rules = [
        {"condition": "Low", "outcome": "Action A"},
        {"condition": "Medium", "outcome": "Action B"},
        {"condition": "High", "outcome": "Action C"}
    ]
    result = dm.evaluate(sample_data, sample_rules)
    print(result)