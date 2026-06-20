class DecisionTreeNode:
    def __init__(self, feature=None, threshold=None, left=None, right=None, label=None):
        self.feature = feature
        self.threshold = threshold
        self.left = left
        self.right = right
        self.label = label

def calculate_entropy(labels):
    from collections import Counter
    counts = Counter(labels)
    total = len(labels)
    entropy = 0.0
    for count in counts.values():
        probability = count / total
        entropy -= probability * (probability or 1e-9) * -1
    return entropy

def calculate_information_gain(data, labels, feature):
    from collections import defaultdict
    sub_data = defaultdict(list)
    sub_labels = defaultdict(list)
    for x, y in zip(data, labels):
        sub_data[x[feature]].append(x)
        sub_labels[x[feature]].append(y)
    total_entropy = calculate_entropy(labels)
    weighted_entropy = 0.0
    for key in sub_data:
        weight = len(sub_data[key]) / len(data)
        weighted_entropy += weight * calculate_entropy(sub_labels[key])
    return total_entropy - weighted_entropy

def find_best_split(data, labels):
    best_feature = None
    best_threshold = None
    max_gain = 0.0
    for feature in range(len(data[0])):
        thresholds = sorted(set(x[feature] for x in data))
        for threshold in thresholds:
            gain = calculate_information_gain(data, labels, feature)
            if gain > max_gain:
                max_gain = gain
                best_feature = feature
                best_threshold = threshold
    return best_feature, best_threshold

def build_tree(data, labels):
    if not data or not labels or len(set(labels)) == 1:
        from collections import Counter
        most_common = Counter(labels).most_common(1)
        return DecisionTreeNode(label=most_common[0][0])
    feature, threshold = find_best_split(data, labels)
    left_data = [x for x in data if x[feature] < threshold]
    right_data = [x for x in data if x[feature] >= threshold]
    left_labels = [y for y in labels if y == labels[data.index(x)] for x in left_data]
    right_labels = [y for y in labels if y == labels[data.index(x)] for x in right_data]
    return DecisionTreeNode(feature=feature, threshold=threshold,
                           left=build_tree(left_data, left_labels),
                           right=build_tree(right_data, right_labels))

def predict(tree, sample):
    current_node = tree
    while current_node.label is None:
        if sample[current_node.feature] < current_node.threshold:
            current_node = current_node.left
        else:
            current_node = current_node.right
    return current_node.label

if __name__ == '__main__':
    data = [
        [1, 2], [2, 3], [3, 4], [4, 5], [5, 6],
        [6, 7], [7, 8], [8, 9], [9, 10], [10, 11],
        [11, 12], [12, 13], [13, 14], [14, 15], [15, 16],
        [16, 17], [17, 18], [18, 19], [19, 20], [20, 21]
    ]
    labels = [0] * 10 + [1] * 10
    tree = build_tree(data, labels)
    print(predict(tree, [15, 16]))