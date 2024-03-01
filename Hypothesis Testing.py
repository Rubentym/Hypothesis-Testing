import scipy.stats as stats

def hypothesis_testing(data1, data2):
    t_statistic, p_value = stats.ttest_ind(data1, data2)
    return t_statistic, p_value

# Example usage:
data1 = [1, 2, 3, 4, 5]
data2 = [2, 4, 6, 8, 10]
t_statistic, p_value = hypothesis_testing(data1, data2)
print("T-statistic:", t_statistic)
print("P-value:", p_value)
