#Sort dictionary in ascending and descending order

dict={"Aparna":7,"hridya":21,"megha":2,"nidhina":8,"nandhana":12,"anusree":1,"reema":18,"athira":17,"vismaya":5}
l1=list(dict.items())
l1.sort()
print("Dictionary in ascending order : ",l1)

l2=list(dict.items())
l2.sort(reverse=True)
print("Dictionary in descending order : ",l2)
