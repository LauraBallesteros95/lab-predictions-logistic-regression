import imblearn
import pymysql
from sqlalchemy import create_engine
import pandas as pd
import numpy as np
import getpass
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import Normalizer, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.preprocessing import OneHotEncoder

password = getpass.getpass()

connection_string = 'mysql+pymysql://root:' + password + '@localhost/sakila'
engine = create_engine(connection_string)

query = '''
        SELECT f.film_id, f.length, f.rating, f.special_features, f.rental_duration, f.rental_rate, r.inventory_id, 
       CASE 
           WHEN p.customer_id IS NOT NULL THEN 1
           ELSE 0
       END AS label
FROM film AS f
JOIN inventory AS i ON f.film_id = i.film_id
JOIN rental AS r ON i.inventory_id = r.inventory_id
LEFT JOIN payment AS p ON r.rental_id = p.rental_id;
        '''

data = pd.read_sql_query(query, engine)
data

