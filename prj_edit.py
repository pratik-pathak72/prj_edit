#file object
#takes the input name od the file along with the extension
file_input=input("Enter the name of the file with extension:")
#prints out the name of the file that you typed
print (f"The file you inputted is: {file_input}")
#A general message
print("Copying the hecras files to the same folder......")
#Looking for the lines starting with following names
searchquery='Current Plan', 'Geom File', 'Flow File', 'Plan File'
with open(file_input,"r") as rf:
    with open("example-output_new.prj","w") as wf:
      print ("Creating a new file called example-output_new.prj")
      for line in rf:
          if line.startswith(searchquery):
              wf.write(line)
