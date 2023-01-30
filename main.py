# Monthly expenses
monthly_expenses = {
    'rent': 1200,
    'utilities': 300,
    'transport': 450,
    'food': 600,
    'entertainment': 110,
    'clothing': 220,
    'health': 30,
    'internet': 60,
    'education': 200,
    'other': 100
}

# Calculate the total expenses
def total_expenses(monthly_expenses: dict) -> int:
    """
    Calculate the total expenses
    Args:
        monthly_expenses: dictionary of monthly expenses
    Returns:
        total_expenses: total expenses
    """
    sum=0
    for i in monthly_expenses.values():
        sum+=i

    return sum

# Find the least expensive expense
def least_expensive(monthly_expenses: dict) -> str:
    """
    Find the least expensive expense
    Args:
        monthly_expenses: dictionary of monthly expenses
    Returns:
        least_expensive: least expensive expense
    """
    b=0
    answer=0
    for v in monthly_expenses.values():
        if v>b:
            b=v
    for k in monthly_expenses:
        if monthly_expenses[k]<b:
            b=monthly_expenses[k]
            answer=k


    return answer

# Find the most expensive expense
def most_expensive(monthly_expenses: dict) -> str:
    """
    Find the most expensive expense
    Args:
        monthly_expenses: dictionary of monthly expenses
    Returns:
        most_expensive: most expensive expense
    """
    b=0
    answer=0
    for k in monthly_expenses:
        if monthly_expenses[k]>b:
            b=monthly_expenses[k]
            answer=k
    return answer

print(total_expenses(monthly_expenses))
print(least_expensive(monthly_expenses))
print(most_expensive(monthly_expenses))
