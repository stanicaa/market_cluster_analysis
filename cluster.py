import pandas
from sklearn.cluster import KMeans


#reading the file with the companies and returns data to be analyzed
a=pandas.read_csv('YOUR_CSV_FILE_HERE')
a=a.dropna(axis=0, how='any')

#initializing the data to be clustered. Change the below to fit your data. Basically my data is structured in the columns below
y1=a[['1wk']]
y2=a[['2wk']]
y3=a[['1mo']]
y4=a[['2mo']]
y5=a[['3mo']]

x=a[['Unnamed: 0']].values.tolist()

#defining the number of clusters to break the list into. You 
no_clusters=input('how many clusters do you want? ')
no_clusters=int(no_clusters)

#Manually replace the main variable. Default here is for 2mo, ie y4
## Defining the cluster structure (like how many clusters we want), and dividing the data into clusters
kmeans=KMeans(n_clusters=no_clusters)
output=kmeans.fit(y4)

# combining the clusters with the company codes and printing the clusters
b=[[] for i in range(no_clusters)]

for i in range(no_clusters):
    for j in range(len(output.labels_)):
        if output.labels_[j]==i:
            b[i].append(x[j])

#printing the Clusters
print('THE CLUSTERS')
for k in range(len(b)):
    print('---CLUSTER %s-----' % k)
    print(b[k])

#searching for the cluster of a specific company
co_name=input('the code of the company you are looking for: ')
for k in range(len(b)):
    for j in range(len(b[k])):
        if co_name in b[k][j]:
            print('Company is in cluster %s' % k)
