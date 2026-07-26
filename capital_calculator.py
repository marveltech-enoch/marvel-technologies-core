company_name = "Marvel Technologies"
monthly_revenue = 350000
server_cost = 45000
database_cost = 20000
engineer_salary = 85000 
team_count = 3

print(f"🎯 PROJECT 1: The Capital Calculator v1.0 for {company_name}")

total_engineer_cost = engineer_salary * team_count
total_expenses = server_cost + database_cost + total_engineer_cost
net_profit = monthly_revenue - total_expenses 

print(f"FINAL NET PROFIT: ${net_profit}")
