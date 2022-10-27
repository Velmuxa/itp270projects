#!usr/bin/env/ python3

daily_sales_replaced = daily_sales.replace(";,;", ":::")
daily_transactions = daily_sales_replaced.split(",")

daily_transactions_split = [transaction.split(":::") for transaction in daily_transactions]
transactions_clean = []
for transaction in daily_transactions_split:
  var = []
  for datapoint in transaction:
    var.append(datapoint.strip())
    
  transactions_clean.append(var)

customers = [datapoint[0] for datapoint in transactions_clean]
sales = [datapoint[1] for datapoint in transactions_clean]
thread_sold = [datapoint[2] for datapoint in transactions_clean]
#---------------------------------------------------
total_sales = 0
for sale in sales:
  total_sales += float(sale.strip("$"))
#----------------
thread_sold_split_initial = []
for thread in thread_sold:
  thread_sold_split_initial.append(thread.split("&"))

thread_sold_split = []
for thread in thread_sold_split_initial:
  for i in range(len(thread)):
    thread_sold_split.append(thread[i])
#---
def color_count(color):
  count = 0
  count += thread_sold_split.count(color)
  return count
#==
colors = ['red', 'yellow', 'green', 'white', 'black', 'blue', 'purple']
print("We Sold {count_of_thread} total thread, for a total of ${total_sales}. The colors available were: {colors} and respectively each one's sale count was: {color_count}".format(count_of_thread = len(thread_sold_split), total_sales = total_sales, colors = colors, color_count = [thread_sold_split.count(color) for color in colors]))
