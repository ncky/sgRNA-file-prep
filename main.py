#nyoung | ayoung


inputFile = "gene_list.fasta";
outputFile = "fastaOutput_pyo.txt"
_ = open(inputFile, 'r'); data = _.read(); _.close()

genes = [];
geneNames = [];

buffer = "";
for line in data.splitlines(): # separate genes into separate objects

    if line == data.splitlines()[-1]: #reached end of file
        genes.append(buffer);

    if line == "": #line is empty(next gene)
        if buffer == "": #multiple new lines inbetween genes
            #print("unexpected newline");
            1 == 1;
        else: #append gene to genes list
            genes.append(buffer);
            buffer = ""; #reset buffer
    else:
        buffer += line + "\n"; # add line contents to buffer

for i in range(len(genes)):
    geneNames.append(genes[i].splitlines()[0]) # add gene name to geneName list
    genes[i] = genes[i].split("\n", 1)[1] #remove geneName from genes list

    genes[i] = genes[i].replace('\n', '').replace('\r', ''); #remove all newlines

fileOutBuffer = "";
print("Genes in file: " + str(len(genes)));
for i in range(len(genes)):
    foundlist = [];
    lastchar = "";
    currentchar = "";
    for j in range(len(genes[i])): #find all instances of 'GG'
        currentchar = genes[i][j]
        if lastchar == "G" and currentchar == "G":
            foundlist.append(j);
        lastchar = currentchar;
    #print(geneNames[i]);
    #print(foundlist);
    for j in range(len(foundlist)):
        print(geneNames[i] + "_" + str(j))
        fileOutBuffer += geneNames[i] + "_" + str(j) + "\n";
        if foundlist[j] - 25 < 0 : #not 25 chars before
            print(genes[i][0:foundlist[j] + 5]);
            fileOutBuffer += genes[i][0:foundlist[j] + 5] + "\n";
        else:
            print(genes[i][foundlist[j]-25:foundlist[j]+5]);
            fileOutBuffer += genes[i][foundlist[j]-25:foundlist[j]+5] + "\n";

with open (outputFile, 'w') as f: f.write (fileOutBuffer); #output to file

print("\nDone");