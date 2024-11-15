def calculate_mean(data):
    return sum(data) / len(data)

def calculate_median(data):
    sorted_data = sorted(data)
    n = len(sorted_data)
    if n % 2 == 1:
        return sorted_data[n // 2]
    else:
        return (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2

def calculate_variance(data, mean_value):
    return sum((x - mean_value) ** 2 for x in data) / len(data)

def calculate_standard_deviation(variance_value):
    return variance_value ** 0.5

# Given dataset
data = [8, 6, 16, 18, 4]

# Calculate statistics
mean_value = calculate_mean(data)
median_value = calculate_median(data)
variance_value = calculate_variance(data, mean_value)
std_deviation_value = calculate_standard_deviation(variance_value)

# Output results
print(f"Mean: {mean_value}")
print(f"Median: {median_value}")
print(f"Variance: {variance_value}")
print(f"Standard Deviation: {std_deviation_value}")
