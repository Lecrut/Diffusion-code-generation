class EndValueAnalyzer:
    def __init__(self, records):
        self.records = list(records)
        self._status_map = {
            'valid': 1,
            'invalid': 0,
            'critical': -1
        }

    def _get_status_code(self, status_name):
        return self._status_map.get(status_name, 0)

    def analyze_endpoints(self):
        if len(self.records) < 2:
            raise ValueError("Input list must have at least two items")
        
        first_val = self.records[0]
        last_val = self.records[-1]
        
        if first_val == last_val:
            status = 'valid'
        elif first_val > last_val:
            status = 'critical'
        else:
            status = 'invalid'
            
        code = self._get_status_code(status)
        
        return {
            'first': first_val,
            'last': last_val,
            'difference': first_val - last_val,
            'status_code': code
        }

if __name__ == '__main__':
    data_set = [15, 22, 8, 4, 90]
    analyzer = EndValueAnalyzer(data_set)
    outcome = analyzer.analyze_endpoints()
    print(outcome)