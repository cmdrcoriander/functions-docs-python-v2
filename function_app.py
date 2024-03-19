import logging
import azure.functions as func

app = func.FunctionApp()

@app.blob_trigger(arg_name="myblob", path="test-samples-trigger/inbound/{name}.txt",
                               connection="stscottisaac876203631639_STORAGE") 
def blob_trigger(myblob: func.InputStream):
    logging.info(f"Python blob trigger function processed blob"
                f"Name: {myblob.name}"
                f"Blob Size: {myblob.length} bytes")
