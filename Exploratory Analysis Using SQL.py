#!/usr/bin/env python
# coding: utf-8

# <p style="text-align:center">
#     <a href="https://skills.network/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDS0321ENSkillsNetwork865-2023-01-01">
#     <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/assets/logos/SN_web_lightmode.png" width="200" alt="Skills Network Logo"  />
#     </a>
# </p>
# 
# <h1 align=center><font size = 5>Assignment: SQL Notebook for Peer Assignment</font></h1>
# 
# Estimated time needed: **60** minutes.
# 
# ## Introduction
# Using this Python notebook you will:
# 
# 1.  Understand the Spacex DataSet
# 2.  Load the dataset  into the corresponding table in a Db2 database
# 3.  Execute SQL queries to answer assignment questions 
# 

# ## Overview of the DataSet
# 
# SpaceX has gained worldwide attention for a series of historic milestones. 
# 
# It is the only private company ever to return a spacecraft from low-earth orbit, which it first accomplished in December 2010.
# SpaceX advertises Falcon 9 rocket launches on its website with a cost of 62 million dollars wheras other providers cost upward of 165 million dollars each, much of the savings is because Space X can reuse the first stage. 
# 
# 
# Therefore if we can determine if the first stage will land, we can determine the cost of a launch. 
# 
# This information can be used if an alternate company wants to bid against SpaceX for a rocket launch.
# 
# This dataset includes a record for each payload carried during a SpaceX mission into outer space.
# 

# ### Download the datasets
# 
# This assignment requires you to load the spacex dataset.
# 
# In many cases the dataset to be analyzed is available as a .CSV (comma separated values) file, perhaps on the internet. Click on the link below to download and save the dataset (.CSV file):
# 
#  <a href="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/labs/module_2/data/Spacex.csv" target="_blank">Spacex DataSet</a>
# 
# 

# **Navigate to the Go to UI screen** 
# 
# * Refer to this insruction in this <a href="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/Labs_Coursera_V5/labs/Lab%20-%20Sign%20up%20for%20IBM%20Cloud%20-%20Create%20Db2%20service%20instance%20-%20Get%20started%20with%20the%20Db2%20console/instructional-labs.md.html">link</a> for viewing  the   Go to UI screen. 
# 
# 
# * Later click on **Data link(below SQL)**  in the Go to UI screen  and click on **Load Data** tab.  
# 
# 
# 
# * Later browse for the downloaded spacex file.
# 
# 
# 
# <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/labs/module_2/images/browsefile.png" width="800">
# 
# 
# * Once done select the schema andload the file.  
# 
# 
#  <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/labs/module_2/images/spacexload3.png" width="800">
#  
# 

# 
# If you are facing a problem in uploading the dataset (which is a csv file), you can follow the steps below to upload the .sql file instead of the CSV file:
# 
# * Download the file <a href="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/Spacex%20.sql">Spacex.sql</a>
# 
# * Later click on **SQL** in the  **Go to UI Screen**.
# 
# * Use the **From file** option to browse for the **SQL** file and upload it.
# 
# <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/labs/module_2/images/sqlfile.png">
# 
# * Once you upload the script,you can use the **Run All** option to run all the queries to insert the data.
# 
# <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/labs/module_2/images/runall.png">
# 
#     
# 

# In[1]:


get_ipython().system('pip install --force-reinstall ibm_db==3.1.0 ibm_db_sa==0.3.3')
get_ipython().system('pip install sqlalchemy==1.3.24')
get_ipython().system('pip uninstall ipython-sql -y')
get_ipython().system('pip install ipython-sql==0.4.1')


# ### Connect to the database
# 
# Let us first load the SQL extension and establish a connection with the database
# 

# In[16]:


get_ipython().run_line_magic('load_ext', 'sql')


# 
# 
# 
# **DB2 magic in case of  UI service credentials.**
# 
# 
# 
# <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/labs/module_2/images/servicecredentials.png" width="600">  
# 
# * Use the following format.
# 
# * Add security=SSL at the end
# 
# **%sql ibm_db_sa://my-username:my-password@my-hostname:my-port/my-db-name?security=SSL**
# 

# In[ ]:





# In[17]:


get_ipython().run_line_magic('sql', 'ibm_db_sa://fyr21060:B0wtpF7LUKhsgkwD@b70af05b-76e4-4bca-a1f5-23dbb4c6a74e.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud:32716/BLUDB?security=SSL')


# In[14]:


get_ipython().run_line_magic('sql', 'ibm_db_sa://hlp04433:Xo9GJJsV9nK9wn3Y@2f3279a5-73d1-4859-88f0-a6c3e6b4b907.c3n41cmd0nqnrk39u98g.databases.appdomain.cloud:30756/BLUDB?security=SSL')


# ## Tasks
# 
# Now write and execute SQL queries to solve the assignment tasks.
# 
# ### Task 1
# 
# 
# 
# 
# ##### Display the names of the unique launch sites  in the space mission
# 

# In[20]:


get_ipython().run_cell_magic('sql', 'SELECT DISTINCT LAUNCH_SITE', 'FROM spacex;\n')


# 
# ### Task 2
# 
# 
# #####  Display 5 records where launch sites begin with the string 'CCA' 
# 

# In[ ]:


SELECT *
FROM spacex
WHERE launch_site LIKE 'CCA%'
LIMIT 5;


# ### Task 3
# 
# 
# 
# 
# ##### Display the total payload mass carried by boosters launched by NASA (CRS)
# 

# In[ ]:


SELECT SUM(payload_mass_kg_) AS total_payload_mass
FROM spacex
WHERE customer = 'NASA (CRS)';


# ### Task 4
# 
# 
# 
# 
# ##### Display average payload mass carried by booster version F9 v1.1
# 

# In[ ]:


SELECT AVG(payload_mass_kg_) AS average_payload_mass
FROM spacex
WHERE booster_version = 'F9 v1.1';


# ### Task 5
# 
# ##### List the date when the first successful landing outcome in ground pad was acheived.
# 
# 
# _Hint:Use min function_ 
# 

# In[ ]:


SELECT MIN(date) AS first_successful_landing_date
FROM spacex
WHERE landing_outcome LIKE 'Success (ground pad)';


# ### Task 6
# 
# ##### List the names of the boosters which have success in drone ship and have payload mass greater than 4000 but less than 6000
# 

# In[ ]:


SELECT booster_version
FROM spacex
WHERE landing_outcome = 'Success (drone ship)'
  AND payload_mass_kg_ > 4000
  AND payload_mass_kg_ < 6000;


# ### Task 7
# 
# 
# 
# 
# ##### List the total number of successful and failure mission outcomes
# 

# In[ ]:


SELECT mission_outcome, COUNT(*) AS total_count
FROM spacex
GROUP BY mission_outcome;


# ### Task 8
# 
# 
# 
# ##### List the   names of the booster_versions which have carried the maximum payload mass. Use a subquery
# 

# In[ ]:


SELECT booster_version
FROM spacex
WHERE payload_mass_kg_ = (
  SELECT MAX(payload_mass_kg_)
  FROM spacex
);


# ### Task 9
# 
# 
# ##### List the failed landing_outcomes in drone ship, their booster versions, and launch site names for in year 2015
# 

# In[ ]:


SELECT landing_outcome, booster_version, launch_site
FROM spacex
WHERE landing_outcome LIKE 'Failure%' 
  AND YEAR(date) = 2015;


# ### Task 10
# 
# ##### Rank the count of landing outcomes (such as Failure (drone ship) or Success (ground pad)) between the date 2010-06-04 and 2017-03-20, in descending order
# 

# In[ ]:


SELECT landing_outcome, COUNT(*) AS count
FROM spacex
WHERE date BETWEEN '2010-06-04' AND '2017-03-20'
GROUP BY landing_outcome
ORDER BY count DESC;


# ### Reference Links
# 
# * <a href ="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/Labs_Coursera_V5/labs/Lab%20-%20String%20Patterns%20-%20Sorting%20-%20Grouping/instructional-labs.md.html?origin=www.coursera.org">Hands-on Lab : String Patterns, Sorting and Grouping</a>  
# 
# *  <a  href="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/Labs_Coursera_V5/labs/Lab%20-%20Built-in%20functions%20/Hands-on_Lab__Built-in_Functions.md.html?origin=www.coursera.org">Hands-on Lab: Built-in functions</a>
# 
# *  <a  href="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/Labs_Coursera_V5/labs/Lab%20-%20Sub-queries%20and%20Nested%20SELECTs%20/instructional-labs.md.html?origin=www.coursera.org">Hands-on Lab : Sub-queries and Nested SELECT Statements</a>
# 
# *   <a href="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/Module%205/DB0201EN-Week3-1-3-SQLmagic.ipynb">Hands-on Tutorial: Accessing Databases with SQL magic</a>
# 
# *  <a href= "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/Module%205/DB0201EN-Week3-1-4-Analyzing.ipynb">Hands-on Lab: Analyzing a real World Data Set</a>
# 
# 
# 

# ## Author(s)
# 
# <h4> Lakshmi Holla </h4>
# 

# ## Other Contributors
# 
# <h4> Rav Ahuja </h4>
# 

# ## Change log
# | Date | Version | Changed by | Change Description |
# |------|--------|--------|---------|
# | 2021-10-12 | 0.4 |Lakshmi Holla | Changed markdown|
# | 2021-08-24 | 0.3 |Lakshmi Holla | Added library update|
# | 2021-07-09 | 0.2 |Lakshmi Holla | Changes made in magic sql|
# | 2021-05-20 | 0.1 |Lakshmi Holla | Created Initial Version |
# 

# ## <h3 align="center"> © IBM Corporation 2021. All rights reserved. <h3/>
# 
