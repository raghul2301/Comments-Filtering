import csv

#this function checks whether the given input contains swear words
def find(lst1):
    #open and read csv file using csv module
    file = open("D:/VS/Python/swearwords.csv")
    read = csv.reader(file)

    #declared global variable to use outside the function
    global result
    global lst2

    lst2 = [] #array to store csv file
    result = [] #array which collects the input contains swear words

    #Adding csv file to the list lst2
    for i in read:
        lst2.append(i)

    #checking whether the input exists in csv file or not
    for j in range(len(lst1)):
        for k in range(len(lst2)):
            if lst1[j] == lst2[k][0]:
                result.append(lst1[j])

checking_words = [] #collects number of swear words

#this function checks how many possible ways does the input has been existed in the dataset
def check(word):
    for k in range(len(lst2)):
        for j in range(len(word)):
            if lst2[k][0] in word[j]:
                checking_words.append(lst2[k][0])

inp = input().split() #input function
#calling function
find(inp)
check(inp)

#printing output based on the condition
if len(checking_words) > 0:
    print("we have noticed that your comment contains inapproriate words:")
    print("Swear words involved in your comments:",checking_words)
else:
    print("Your comment has been received!")