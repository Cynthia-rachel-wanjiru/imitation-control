from app.extensions import mongo
print(mongo.db.list_collection_names())
