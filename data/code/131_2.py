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
    sample_data = "sunny"
    sample_rules = [
        {'condition': "sunny", 'outcome': "go to the park"},
        {'condition': "rainy", 'outcome': "stay inside"},
        {'condition': "snowy", 'outcome': "wear a heavy coat"}
    ]
    result = dm.evaluate(sample_data, sample_rules)
    print(result)