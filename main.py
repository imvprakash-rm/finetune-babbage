from openai import OpenAI
client = OpenAI(api_key="your_open_ai_key")

#training_file_name path of training file.json
#validation_file path of validation file.json
# Upload Training and Validation Files
training_file = client.files.create(
    file=open(training_file_name, "rb"), purpose="fine-tune"
)
validation_file = client.files.create(
    file=open(validation_file_name, "rb"), purpose="fine-tune"
)

# Create Fine-Tuning Job
suffix_name = "finetune-docs"
response = client.fine_tuning.jobs.create(
    training_file=training_file.id,
    validation_file=validation_file.id,
    model="babbage-002",
    suffix=suffix_name,
)
