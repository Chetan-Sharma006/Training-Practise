import numpy as np
import matplotlib.pyplot as plt

# Datastructure :[sales- 2021,2022,2023,2024,2025]
sales_data=np.array([
    [1,150000,200000,210000,130000,250000],      #shyam briyani
    [2,100000,250000,200000,300000,150000],      #pizza hut
    [3,160000,300000,400000,350000,280000],      #chai thekka
    [4,250000,600000,450000,280000,300000],      #butter chicken
    [5,450000,300000,700000,380000,490000]       #mayur
])
print("======ZOMATO SALES====")
print(sales_data)
print("sales shape:",sales_data.shape)


while True:
    print("\n choose option:")
    print("1 - Total sales per year")
    print("2 - Minimum sales per resturant")
    print("3 - Maximum sales per resturant")
    print("4 - total sales per resturant")
    print("5 - average sale per restursnt")
    print("6 - maximum sale per year")
    print("7 - cumulative sum")
    print("8 - Ascending order of the sale ")
    print("9 - garph")
    print("10 - exit")

    choice = int(input("Enter your choice:"))
    if choice ==1:
     total_sales=np.sum(sales_data[:,1:],axis=0)
     print("Total sales per resturant:",total_sales)

    elif choice ==2:
     mimsales_resturant=np.min(sales_data[:,1:],axis=1)
     print("minimum sales per resturant:",mimsales_resturant)

    elif choice == 3:
     maxsales_rest=np.max(sales_data[:,1:],axis=1)
     print("Maximum sales per restursnt:",maxsales_rest)

    elif choice == 4:
     totalsales_rest=np.sum(sales_data[:,1:],axis=1)
     print("total sales per resturant:",totalsales_rest)

    elif choice == 5:
     avg_sales=np.mean(sales_data[:,1:],axis=1)
     print("Average sales per resturant:",avg_sales)

    elif choice == 6:
     maxsales_year=np.max(sales_data[:,1:],axis=0)
     print("Maximum sales per year:",maxsales_year)

    elif choice == 7:
     cumsum=np.cumsum(sales_data[:,1:],axis=1)
     print("cumsum of the sales:",cumsum)

    elif choice == 8:
     sort_sales=np.sort(sales_data,axis=1)
     print("Ascending sales as per resturant:",sort_sales)

    elif choice == 9:
     cumsum=np.cumsum(sales_data[:,1:],axis=1)
     plt.figure(figsize=(10,6))
     plt.plot(np.mean(cumsum,axis=0))
     plt.title("Average cumulatives sales of resturant")
     plt.xlabel("years")
     plt.ylabel("sales")
     plt.grid(True)
     plt.show()

    elif choice == 10:
     print("Exiting program...")
    break

else:
 print("Invalid choice \n try again!")